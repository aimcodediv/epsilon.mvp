result = scan_target(target)
click.echo("Scan Results:")
if output == "json":
    click.echo(json.dumps(result, indent=2))
else:
    click.echo(f"Status: {result['status']}")
    click.echo(f"Total Findings: {result['total_findings']}")
    click.echo(f"Severity Breakdown: {result['severity_breakdown']}")
    if result["findings"]:
        click.echo("Findings:")
        for f in result["findings"]:
            click.echo(f"  - {f['vulnerability']} (Severity: {f['severity']}, Confidence: {f['confidence_score']}/10)")
    else:
        click.echo("No vulnerabilities detected.")
