(function () {
  var storageKey = "site-theme";
  var darkTheme = "dark";
  var lightTheme = "light";

  function getPreferredTheme() {
    var savedTheme = localStorage.getItem(storageKey);
    if (savedTheme === darkTheme || savedTheme === lightTheme) {
      return savedTheme;
    }

    return window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches
      ? darkTheme
      : lightTheme;
  }

  function updateThemeColorMeta(theme) {
    var themeMeta = document.querySelector('meta[name="theme-color"]');
    if (!themeMeta) return;
    themeMeta.setAttribute("content", theme === darkTheme ? "#0f172a" : "#ffffff");
  }

  function applyTheme(theme) {
    document.documentElement.setAttribute("data-theme", theme);
    localStorage.setItem(storageKey, theme);
    updateThemeColorMeta(theme);

    var button = document.getElementById("theme-toggle");
    if (!button) return;

    var isDark = theme === darkTheme;
    button.textContent = isDark ? "☀️" : "🌙";
    button.setAttribute("aria-label", isDark ? "Switch to light mode" : "Switch to dark mode");
    button.setAttribute("title", isDark ? "Switch to light mode" : "Switch to dark mode");
  }

  document.addEventListener("DOMContentLoaded", function () {
    applyTheme(getPreferredTheme());

    var button = document.getElementById("theme-toggle");
    if (!button) return;

    button.addEventListener("click", function () {
      var currentTheme = document.documentElement.getAttribute("data-theme") || lightTheme;
      applyTheme(currentTheme === darkTheme ? lightTheme : darkTheme);
    });
  });
})();
