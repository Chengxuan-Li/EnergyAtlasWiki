# Plotting Playground

Use this tool to design and preview your [Ploly.js](https://plotly.com/javascript/reference/index/) chart and embed it in a wiki page.

Edit the JSON below and the chart will render live. For quick start examples check out [Plotting Guide](plotting-guide.md)



<div class="plotly-playground" data-plotly-playground>
  <div class="plotly-playground-chart plotly-chart"></div>
  <div class="plotly-playground-error"></div>
  <div class="code-block-container">
    <div class="code-block-inner">
      <div class="code-block-header">
        <span class="code-block-lang">json</span>
        <button class="plotly-playground-copy copy-button" type="button">Copy</button>
      </div>
      <div class="code-block-sep"></div>
      <div class="code-block-body">
        <div class="code-block-content">
          <textarea class="plotly-playground-editor" rows="16">{
  "title": "Playground chart",
  "subtitle": "Edit the JSON to see changes",
  "data": [
    {
      "type": "scatter",
      "mode": "lines+markers",
      "name": "Series A",
      "x": [1, 2, 3, 4, 5],
      "y": [10, 14, 12, 16, 18]
    },
    {
      "type": "bar",
      "name": "Series B",
      "x": [1, 2, 3, 4, 5],
      "y": [8, 11, 9, 13, 15]
    }
  ],
  "layout": {
    "xaxis": {"title": "Step"},
    "yaxis": {"title": "Value"},
    "barmode": "group"
  }
}</textarea>
        </div>
      </div>
    </div>
  </div>
</div>
