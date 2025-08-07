function isMobile() {
    return window.innerWidth <= 1024; 
}

function resizeFlipbook() {
    if (isMobile()) {
        const screenWidth = window.innerWidth;
        const screenHeight = window.innerHeight;

        let bookWidth = screenWidth * 0.95;
        let bookHeight = bookWidth * 0.6;

        if (bookHeight > screenHeight * 0.9) {
            bookHeight = screenHeight * 0.9;
            bookWidth = bookHeight / 0.6;
        }

        $(".flipbook").turn("size", bookWidth, bookHeight);
        $(".flipbook").css({
            width: bookWidth + "px",
            height: bookHeight + "px"
        });
    } else {
        // Tamanho padrão para desktop
        $(".flipbook").turn("size", 1000, 600);
        $(".flipbook").css({
            width: "1000px",
            height: "600px"
        });
    }
}

$(document).ready(function () {
    $(".flipbook").turn({
        width: 1000,
        height: 600,
        autoCenter: true,
        elevation: 50,
        gradients: true
    });

    resizeFlipbook();

    $(window).on("resize orientationchange", function () {
        resizeFlipbook();
    });
});