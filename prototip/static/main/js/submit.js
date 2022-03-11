function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
const csrftoken = getCookie("csrftoken");

{
  /*$("#contact-form").on("submit", function (e) {
  e.preventDefault();
  $.ajax({
    headers: { "X-CSRFToken": csrftoken },
    method: "POST",
    url: "",
    data: {
      name: $("#name").val(),
      email: $("#email").val(),
      subject: $("#subject").val(),
      message: $("#message").val(),
      dataType: "json",
    },

    success: function (res) {
      $(".massage").text(res.massage);
    },
    error: function (response) {
      // alert the error if any error occured
      alert(response);
    },
  });
});*/
}
