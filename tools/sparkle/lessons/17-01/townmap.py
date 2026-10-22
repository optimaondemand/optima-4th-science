# the Palmetto Springs town map (viewBox 600x380), shared by the case file and the storm clock
def P(x, y, t, size=11, fill='#14254D', bg='#F4EBD6'):
    w = len(t) * size * 0.64 + 14
    return f'<rect x="{x - w/2:.0f}" y="{y - size - 2}" width="{w:.0f}" height="{size + 7}" rx="5" fill="{bg}" opacity=".93"/>' + T(x, y + 1, t, size, fill, 'middle', 900)
def T(x, y, t, size=13, fill='#F2F5F9', anchor='middle', w=800):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{w}" fill="{fill}" font-family="Nunito,sans-serif">{t}</text>'
s = ['<svg viewBox="0 0 600 380" role="img" aria-label="A map of Palmetto Springs: the bay along the bottom with Bay Street and the dock, the Cypress Slough wetland on the left, the spring at the top left, and Pine Avenue, Main Street, Oak Street and Elm Street in town.">']
s.append('<rect width="600" height="380" fill="#3E5A3A"/>')
# land texture: blocks
s.append('<path d="M0 0H600V300Q520 286 450 300T300 296T150 304T0 296Z" fill="#53704A"/>')
# the bay
s.append('<path d="M0 300Q75 290 150 304T300 296T450 300T600 292V380H0Z" fill="#2C6E9E"/>')
s.append('<path d="M0 318Q90 310 170 320T340 314T600 310" fill="none" stroke="#5E9CC8" stroke-width="2" opacity=".6"/><path d="M0 344Q110 336 220 346T430 340T600 338" fill="none" stroke="#5E9CC8" stroke-width="2" opacity=".5"/>')
s.append(T(110, 352, 'THE BAY', 15, '#CFE6F7'))
# evacuation zone along Bay Street
s.append('<path d="M190 300V246H600V292Q520 286 450 300T300 296T190 302Z" fill="#D9342B" fill-opacity=".22" stroke="#FF8A80" stroke-width="2" stroke-dasharray="6 4"/>')
s.append(P(405, 240, 'EVACUATION ZONE', 10, '#fff', '#C62828'))
# Cypress Slough wetland
s.append('<path d="M10 180Q60 160 120 176T190 210L196 300Q120 306 10 298Z" fill="#6E8F4E"/>')
for x, y in [(40, 210), (70, 236), (140, 250), (60, 270), (160, 280), (95, 262), (30, 250)]:
    s.append(f'<path d="M{x} {y}v-12M{x-5} {y}l3-10M{x+5} {y}l-3-10" stroke="#C9DDA3" stroke-width="2" stroke-linecap="round"/>')
s.append(T(100, 196, 'Cypress Slough', 13, '#EAF4D6'))
s.append(T(100, 210, '(wetland)', 10, '#EAF4D6'))
# the spring
s.append('<ellipse cx="110" cy="70" rx="38" ry="22" fill="#3FA7C9" stroke="#BDE8F5" stroke-width="2"/><path d="M110 92Q100 130 120 176" fill="none" stroke="#3FA7C9" stroke-width="5"/>')
s.append(T(110, 40, 'Palmetto Spring', 13))
# roads
road = 'stroke="#D9D2BC" stroke-linecap="round" fill="none"'
s.append(f'<path d="M200 278H600" {road} stroke-width="9"/>')            # Bay Street
s.append(f'<path d="M300 30V278" {road} stroke-width="9"/>')              # Pine Ave
s.append(f'<path d="M200 200H600" {road} stroke-width="9"/>')            # Main Street
s.append(f'<path d="M300 140H600" {road} stroke-width="7"/>')            # Oak Street
s.append(f'<path d="M330 80H600" {road} stroke-width="7"/>')             # Elm Street
s.append(f'<path d="M200 200V278" {road} stroke-width="7"/>')
s.append(P(545, 283, 'Bay Street'))
s.append(P(300, 22, 'Pine Ave'))
s.append(P(545, 205, 'Main Street'))
s.append(P(545, 145, 'Oak Street'))
s.append(P(545, 85, 'Elm Street'))
# houses
for x in range(222, 600, 30):
    if 500 < x < 590: continue
    s.append(f'<rect x="{x}" y="256" width="16" height="14" rx="2" fill="#E9E1CF"/><path d="M{x-2} 257l10-8 10 8z" fill="#B66A4A"/>')
for x in range(340, 600, 34):
    if x > 480: continue
    s.append(f'<rect x="{x}" y="94" width="15" height="13" rx="2" fill="#E9E1CF"/><rect x="{x+4}" y="150" width="15" height="13" rx="2" fill="#E9E1CF"/>')
# town hall
s.append('<rect x="232" y="160" width="40" height="28" fill="#F2EAD6" stroke="#8C7B5A" stroke-width="2"/><path d="M228 162l24-14 24 14z" fill="#8C7B5A"/>')
s.append(T(252, 152, 'Town hall', 10, '#F2F5F9'))
# the dock + tide gauge
s.append('<rect x="414" y="284" width="12" height="44" fill="#8C6A44"/><rect x="404" y="324" width="32" height="8" fill="#8C6A44"/>')
s.append('<rect x="432" y="296" width="6" height="40" fill="#F5F5F5" stroke="#333" stroke-width="1"/><path d="M432 304h6M432 312h6M432 320h6M432 328h6" stroke="#333"/>')
s.append(P(470, 360, 'Dock + tide gauge', 10))
s.append('<g class="fs-sn-pins"></g></svg>')
MAP = ''.join(s)
if __name__ == '__main__':
    open('townmap.svg', 'w').write(MAP); print(len(MAP))
