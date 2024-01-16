anlysis_prompt = """evaluate the marketing effectiveness of this landing page. Generate a list of 5 suggestions in json, return only the json without anything else.

Output example:
{
  "suggestions": [
    {
      "element": "Headline",
      "suggestion": "Make the headline more specific to the product or service offered to better capture user interest and improve targeting."
    },
    {
      "element": "Value Proposition",
      "suggestion": "Include a more detailed description of benefits and features to clearly communicate the value proposition to visitors."
    },
    {
      "element": "Hero Image",
      "suggestion": "Replace the placeholder with an actual high-quality image or graphic that represents the product or service effectively."
    },
    {
      "element": "Call to Action (CTA)",
      "suggestion": "Make the CTA button more prominent with contrasting colors and actionable text that encourages clicks."
    },
    {
      "element": "Social Proof",
      "suggestion": "Show actual customer testimonials or case studies instead of just a rating to add authenticity and trustworthiness."
    }
  ]
}
"""