import panflute as pf

_unicode_tex_replaces = {
    '≤': r'\leq{}', '≥': r'\geq{}',
    '≠': r'\neq{}', '≈': r'\approx{}',
    '×': r'\times{}', '÷': r'\div{}',
    '±': r'\pm{}', '·': r'\cdot{}',
    '◦': r'\circ{}', '′': r'\prime{}',
    '∞': r'\infty{}', '¬': r'\neg{}',
    '∧': r'\wedge{}', '∨': r'\vee{}',
    '⊃': r'\supset{}', '∀': r'\forall{}',
    '∈': r'\in{}', '→': r'\rightarrow{}',
    '⊂': r'\subset{}', '∃': r'\exists{}',
    '∉': r'\notin{}', '⇒': r'\Rightarrow{}',
    '∪': r'\cup{}', '∩': r'\cap{}',
    '|': r'\mid{}', '⇔': r'\Leftrightarrow{}',
    '≃': r'\simeq{}', '≳': r'\gtrsim{}',
    '≲': r'\lesssim{}',

    'α': r'\alpha{}', 'β': r'\beta{}',
    'γ': r'\gamma{}', 'δ': r'\delta{}',
    '∊': r'\epsilon{}', 'ζ': r'\zeta{}',
    'η': r'\eta{}', 'ε': r'\varepsilon{}',
    'θ': r'\theta{}', 'ι': r'\iota{}',
    'κ': r'\kappa{}', '𝜗': r'\vartheta{}',
    'λ': r'\lambda{}', 'μ': r'\mu{}',
    'ν': r'\nu{}', 'ξ': r'\xi{}',
    'π': r'\pi{}', 'ρ': r'\rho{}',
    'σ': r'\sigma{}', 'τ': r'\tau{}',
    'υ': r'\upsilon{}', 'φ': r'\phi{}',
    'χ': r'\chi{}', 'ψ': r'\psi{}',
    'ω': r'\omega{}',
    'Γ': r'\Gamma{}', 'Δ': r'\Delta{}',
    'Θ': r'\Theta{}', 'Λ': r'\Lambda{}',
    'Ξ': r'\Xi{}', 'Π': r'\Pi{}',
    'Σ': r'\Sigma{}', 'Υ': r'\Upsilon{}',
    'Φ': r'\Phi{}', 'Ψ': r'\Psi{}',
    'Ω': r'\Omega{}',
}

def unicode_replace(elem, doc):
    if hasattr(elem, 'text'):
        found_chars = [key for key in _unicode_tex_replaces.keys()
                       if key in elem.text]
        for u_char in found_chars:
            elem.text = elem.text.replace(
                u_char, _unicode_tex_replaces[u_char])
        if len(found_chars) and type(elem) != pf.Math:
            return pf.Math(text=elem.text, format='InlineMath')
    return


if __name__ == '__main__':
    pf.toJSONFilter(unicode_replace)
