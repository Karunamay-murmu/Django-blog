tinymce.init({
    selector: 'textarea#id_body',
    skin: "CUSTOM",
    content_css: "CUSTOM",
    height: 600,
    menubar: false,
    plugins: 'print preview paste searchreplace autolink autosave save directionality code visualblocks visualchars fullscreen image link media template codesample table charmap hr pagebreak nonbreaking anchor toc insertdatetime advlist lists wordcount imagetools textpattern noneditable help charmap quickbars emoticons',
    toolbar: 'formatselect| bold italic underline strikethrough table | alignleft aligncenter alignright alignjustify | outdent indent |  numlist bullist | forecolor backcolor removeformat | pagebreak | charmap emoticons | fullscreen  preview | insertfile image media link anchor codesample searchreplace',
    images_upload_url: '/',
    images_upload_handler: function (blobid, success, failed) {
        if (!failed) {
            success.onload = this.blobid({
                
            })
        }
    }
});
