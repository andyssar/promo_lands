(function ($) {
  var cases = {
    seo: {
      label: "SEO Monitoring",
      title: "Collect local SERP data without unstable access",
      text: "Compare desktop and mobile search results, track rankings across locations, and keep SEO monitoring jobs running with real IPs.",
      features: [
        ["Local results", "Target countries, regions, and city-level markets."],
        ["Real IPs", "Mimic real user searches and reduce detection risk."],
        ["REST API", "Automate extraction from existing pipelines."]
      ]
    },
    scraping: {
      label: "Data Scraping",
      title: "Extract public web data at scale with fewer interruptions",
      text: "Avoid bans and rate limits while collecting valuable website data for analytics, pricing, catalog monitoring, and internal tools.",
      features: [
        ["Geo-targeting", "Collect regionally varied or restricted content."],
        ["IP rotation", "Rotate automatically to keep collection jobs moving."],
        ["Simple integration", "Use proxy credentials in existing scraping software."]
      ]
    },
    ads: {
      label: "Ad Verification",
      title: "Verify ad delivery from the markets that matter",
      text: "Check placements, detect fraud, and monitor brand safety through real residential and mobile network signals.",
      features: [
        ["Brand safety", "Monitor placements across regions and publishers."],
        ["Fraud checks", "Mimic real user devices to verify delivery quality."],
        ["Global coverage", "Choose locations to confirm ads appear correctly."]
      ]
    },
    market: {
      label: "Market Research",
      title: "Research competitors, sentiment, and local demand",
      text: "Access target websites and public platforms without blocks, then collect market signals for planning and strategy.",
      features: [
        ["Social analysis", "Track public sentiment on social platforms and forums."],
        ["Global access", "Analyze trends in different markets."],
        ["SERP scraping", "Identify opportunities and changing consumer needs."]
      ]
    },
    ai: {
      label: "AI and LLM Data",
      title: "Collect diverse public data for AI workflows",
      text: "Support AI training, evaluation, and retrieval workflows with scalable proxy access and responsible data collection controls.",
      features: [
        ["Ethical network", "Use consent-based IPs for long-term stability."],
        ["Global datasets", "Create broader datasets from many regions."],
        ["Scalable pipelines", "Use PAYG pricing and API-friendly access."]
      ]
    }
  };

  function renderCase(key) {
    var item = cases[key] || cases.seo;
    var $panel = $("[data-case-panel]");
    var featureHtml = item.features.map(function (feature) {
      return "<div><strong>" + feature[0] + "</strong><span>" + feature[1] + "</span></div>";
    }).join("");

    $panel.fadeOut(120, function () {
      $panel.html(
        "<div>" +
          "<span class=\"eyebrow\">" + item.label + "</span>" +
          "<h3>" + item.title + "</h3>" +
          "<p>" + item.text + "</p>" +
        "</div>" +
        "<div class=\"feature-stack\">" + featureHtml + "</div>"
      ).fadeIn(140);
    });
  }

  $("[data-menu-toggle]").on("click", function () {
    $("[data-nav]").toggleClass("open");
  });

  $(".main-nav a").on("click", function () {
    $("[data-nav]").removeClass("open");
  });

  $(".usecase-tabs button").on("click", function () {
    var key = $(this).data("case");
    $(".usecase-tabs button").removeClass("active");
    $(this).addClass("active");
    renderCase(key);
  });

  $("[data-accordion] button").on("click", function () {
    var $item = $(this).closest("article");
    var $content = $item.find("p");

    if ($item.hasClass("open")) {
      $item.removeClass("open");
      $content.stop(true, true).slideUp(180);
    } else {
      $item.addClass("open");
      $content.stop(true, true).hide().slideDown(180);
    }
  });

  $("[data-copy]").on("click", function () {
    var selector = $(this).data("copy");
    var text = $(selector).text();
    var $button = $(this);

    if (navigator.clipboard) {
      navigator.clipboard.writeText(text).then(function () {
        $button.text("Copied");
        setTimeout(function () {
          $button.text("Copy");
        }, 1200);
      });
    }
  });
})(jQuery);
