function UsageTrendChart({ points = [] }) {
  if (!points.length) {
    return (
      <div className="trend-chart-empty">
        <p>No usage history yet.</p>
        <p>Analyze your recent units to see a trend chart here.</p>
      </div>
    );
  }

  const width = 320;
  const height = 160;
  const padding = 24;
  const maxValue = Math.max(...points, 1);
  const minValue = Math.min(...points, 0);
  const range = maxValue === minValue ? 1 : maxValue - minValue;
  const plotWidth = width - padding * 2;
  const plotHeight = height - padding * 2;

  const pointsString = points
    .map((value, index) => {
      const x = padding + (plotWidth * index) / Math.max(points.length - 1, 1);
      const y = padding + ((maxValue - value) / range) * plotHeight;
      return `${x},${y}`;
    })
    .join(' ');

  const first = points[0];
  const last = points[points.length - 1];
  const trendLabel = last > first ? 'Rising' : last < first ? 'Falling' : 'Stable';

  return (
    <div className="trend-chart">
      <div className="trend-chart-header">
        <h3>Usage trend</h3>
        <span className={`trend-pill ${trendLabel.toLowerCase()}`}>{trendLabel}</span>
      </div>
      <svg viewBox={`0 0 ${width} ${height}`} className="chart-svg" aria-label="Usage trend chart">
        <polyline
          fill="none"
          stroke="rgba(56, 189, 248, 0.95)"
          strokeWidth="4"
          strokeLinecap="round"
          strokeLinejoin="round"
          points={pointsString}
        />
        {points.map((value, index) => {
          const x = padding + (plotWidth * index) / Math.max(points.length - 1, 1);
          const y = padding + ((maxValue - value) / range) * plotHeight;
          return (
            <circle key={index} cx={x} cy={y} r="4.5" fill="#fff" stroke="#38bdf8" strokeWidth="2" />
          );
        })}
        <line x1={padding} y1={padding} x2={padding} y2={height - padding} stroke="rgba(148, 163, 184, 0.2)" />
        <line x1={padding} y1={height - padding} x2={width - padding} y2={height - padding} stroke="rgba(148, 163, 184, 0.2)" />
      </svg>
      <div className="trend-chart-footer">
        <span>Latest: {last} units</span>
        <span>Range: {minValue} - {maxValue}</span>
      </div>
    </div>
  );
}

export default UsageTrendChart;
