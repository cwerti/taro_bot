function handleFormSubmit(event) {
  event.preventDefault()
}


const postData = async (url = '', data = {}) => {
  // Формируем запрос
  const response = await fetch(url, {
    // Метод, если не указывать, будет использоваться GET
    method: 'POST',
   // Заголовок запроса
    headers: {
      'Content-Type': 'application/json'
    },
    // Данные
    body: JSON.stringify(data)
  });
  return response.json();
}


function deleteAllCookies() {
    document.cookie.split(';').forEach(cookie => {
        const eqPos = cookie.indexOf('=');
        const name = eqPos > -1 ? cookie.substring(0, eqPos) : cookie;
        document.cookie = name + '=;expires=Thu, 01 Jan 1970 00:00:00 GMT';
    });
}

function getCookie(name) {
  let cookie = document.cookie.split('; ').find(row => row.startsWith(name + '='));
  return cookie ? cookie.split('=')[1] : null;
}


function serializeForm(formNode) {
  const { elements } = formNode
  const data = Array.from(elements)
    .filter((item) => !!item.name)
    .map((element) => {
      const { name, type } = element
      const value = type === 'checkbox' ? element.checked : element.value
      return { name, value }
    })
  console.log(data);

  document.cookie =`data=${data[0].value}`
  document.cookie = `yesCount=0`

  let elem = document.getElementById('slider');
  let img = document.createElement('img');
  img.className = "thumb"
  img.src = "../static/images/cards/info.png"
  img.style = "position: absolute; left: 28%;"
  elem.append(img);
  let thumb = slider.querySelector('.thumb');
  console.log(thumb);
  thumb.onmousedown = function(event) {
      event.preventDefault(); // предотвратить запуск выделения (действие браузера)
      thumb.style.opacity = '100%';
      thumb.style.animationFillMode = 'none';
      thumb.style.transition = 'none';
      thumb.style.animationDelay = '0s';
      thumb.style.animation = 'none';
      let shiftX = event.clientX - thumb.getBoundingClientRect().left;
      // shiftY здесь не нужен, слайдер двигается только по горизонтали
      document.addEventListener('mousemove', onMouseMove);
      document.addEventListener('mouseup', onMouseUp);
      function onMouseMove(event) {
        let newLeft = (event.clientX - shiftX - slider.getBoundingClientRect().left) - 120;

        let rightEdge = slider.offsetWidth - thumb.offsetWidth;
        thumb.style.transform = `translate(${newLeft * 0.4}px, 0px) rotateX(${newLeft* 0.02}deg) rotateY(${newLeft* 0.02}deg) rotateZ(${newLeft* 0.02}deg )`;

        if (newLeft > 120){
            console.log();
        }
        if (newLeft < -120){
            console.log();
        }
      }

      function onMouseUp(event) {
        let newLeft = (event.clientX - shiftX - slider.getBoundingClientRect().left) - 120;
        console.log(newLeft);
        if (Math.abs(newLeft) <= 140){
            newLeft = 0;
            thumb.style.transition = `transform 1s`;
            thumb.style.transform = `translate(${newLeft * 0.4}px, 0px) rotateX(${newLeft* 0.02}deg) rotateY(${newLeft* 0.02}deg) rotateZ(${newLeft* 0.02}deg )`;
        }
        else{
            if (newLeft < -140){
                thumb.style.opacity = '100%';
                thumb.style.animationFillMode = '';
                thumb.style.transition = '';
                thumb.style.animationDelay = '';
                thumb.style.animation = '';
                thumb.className = 'thumb';
                thumb.id = "leave"

            }
            if (newLeft > 140){
                thumb.style.opacity = '100%';
                thumb.style.animationFillMode = '';
                thumb.style.transition = '';
                thumb.style.animationDelay = '';
                thumb.style.animation = '';
                thumb.className = 'thumb';
                thumb.id = "leave"
                document.cookie = `yesCount=${Number(getCookie("yesCount")) + 1}`
            }
        }

        document.removeEventListener('mouseup', onMouseUp);
        document.removeEventListener('mousemove', onMouseMove);
      }

      thumb.addEventListener('webkitAnimationEnd', function(){
            if (thumb.id !== ''){
                thumb.remove();
                img.style.transform = '';
                img.id = '';
                if (getCookie("yesCount") !== '3'){
                    elem.append(img)
                    console.log(img.style.position);
                    }
                else{
                    console.log(document.cookie);
                    postData('../postdata', { data: getCookie("data")})
                      .then((data) => {
                        console.log(data);
                      });
                }
            }
        }, true);

    };


    thumb.ondragstart = function() {
      return false;
    };

}



function handleFormSubmit(event) {
  event.preventDefault()
  serializeForm(applicantForm)
}

const applicantForm = document.getElementById('mars-once')
applicantForm.addEventListener('submit', handleFormSubmit)
