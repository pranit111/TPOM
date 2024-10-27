$(document).ready(function() {
    // Function to load content via AJAX
    function loadContent(url) {
        $.ajax({
            url: url,
            type: 'GET',
            success: function(data) {
                $('.dashboard-main').html(data);  // Replace the main content area with new content
            },
            error: function() {
                alert('Error loading content');
            }
        });
    }

    // Attach click event to sidebar links
    $('.sidebar a').on('click', function(e) {
        e.preventDefault();
        var url = $(this).data('url');
        loadContent(url);
    });

    // Load the default content (Overview) on page load
    loadContent("{% url 'overview' %}");
});
 function loadContent(url) {
    $('.dashboard-main').html('<p>Loading...</p>');  // Show loading message

    $.ajax({
        url: url,
        type: 'GET',
        success: function(data) {
            $('.dashboard-main').html(data);  // Replace with new content
        },
        error: function() {
            $('.dashboard-main').html('<p>Error loading content</p>');  // Show error message
        }
    });
}


