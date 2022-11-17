function viewList()
{
    var restaurantBox = document.querySelectorAll('.restaurant');

    for(var i=0; i<restaurantBox.length; i++)
    {
        if (restaurantBox[i].style.display == 'none') 
        {
            restaurantBox[i].style.display='block';
            document.getElementById('list_button').innerText='리스트 숨기기'
        }

        else 
        {
            restaurantBox[i].style.display='none';
            document.getElementById('list_button').innerText='리스트 보기'
        }
        
    }
}
