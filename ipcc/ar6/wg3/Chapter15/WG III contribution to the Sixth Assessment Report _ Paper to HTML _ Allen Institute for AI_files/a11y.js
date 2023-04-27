$(document).ready(function () {
    //Theme Toggler
    $(".js-themer").on("click", function (e) {
        event.stopPropagation();

        var $this = $(this);
        var theme = $this.attr("data-theme")

        $(".js-themer").removeClass("on");
        $this.addClass("on");
        $("body").removeClass(function (index, className) {
            return (className.match(/(^|\s)theme--\S+/g) || []).join(' ');
        }).addClass(theme);

        e.preventDefault();
    });


    //Aid Toggler
    $(".js-aid").on("click", function (e) {
        event.stopPropagation();

        var $this = $(this);
        var aid = $this.attr("data-aid")

        $(".js-aid").removeClass("on");
        $this.addClass("on");
        $("html").removeClass(function (index, className) {
            return (className.match(/(^|\s)aid--\S+/g) || []).join(' ');
        }).addClass(aid);

        e.preventDefault();
    });


    // Dropdown Toggler
    $(".dropdown-toggler").on("click", function (e) {
        event.stopPropagation();

        var $this = $(this);

        if ($this.parent().hasClass("on")) {
            $this.parent().removeClass("on");
        } else {
            $(".dropdown.on").removeClass("on");
            $this.parent().addClass("on");
        }

        e.preventDefault();
    });

    $(window).click(function () {
        $(".dropdown.on").removeClass("on");
    });

    $(".js-toc-toggle").on("click", function (e) {
        $(".paper__nav").addClass("on");
        e.preventDefault();
    });

    $(".paper__nav").on("click", function () {
        $(".paper__nav").removeClass("on");
    });

    $("input[name='file']").change(
        function () {
            $("button[name='uploadButton']").attr('disabled', !$(this).val());
            $("button[name='uploadButton']").attr('aria-disabled', !$(this).val());
        }
    );

    $("form").on("submit", function () {
        $("button[name='uploadButton']").attr("disabled", true);
        $("button[name='uploadButton']").attr("aria-disabled", true);
        $("button[name='uploadButton']").html("Processing...");
    });
});


window.addEventListener("hashchange", function () {
    window.scrollTo(window.scrollX, window.scrollY - 100);
});