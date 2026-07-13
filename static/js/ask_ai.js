<script>

const chips=document.querySelectorAll(".chip");

const textarea=document.querySelector("textarea");

chips.forEach(chip=>{

    chip.addEventListener("click",()=>{

        textarea.value=chip.innerText;

        textarea.focus();

    });

});

</script>