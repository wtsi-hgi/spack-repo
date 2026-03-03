# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConcstats(RPackage):
	"""Market Structure, Concentration and Inequality Measures

	Based on individual market shares of all participants in a
    market or space, the package offers a set of different structural and
    concentration measures frequently - and not so frequently - used in research
    and in practice. Measures can be calculated in groups or individually.
    The calculated measure or the resulting vector in table format should help
    practitioners make more informed decisions. Methods used in this package are
    from:
    1.  Chang, E. J., Guerra, S. M., de Souza Penaloza, R. A. & Tabak, B. M.
    (2005) "Banking concentration: the Brazilian case".
    2.  Cobham, A. and A. Summer (2013). "Is It All About the Tails? The
    Palma Measure of Income Inequality".
    3.  Garcia Alba Idunate, P. (1994). "Un Indice de dominancia para el
    analisis de la estructura de los mercados".
    4.  Ginevicius, R. and S. Cirba (2009). "Additive measurement of market
    concentration" <doi:10.3846/1611-1699.2009.10.191-198>.
    5.  Herfindahl, O. C. (1950), "Concentration in the steel industry"
    (PhD thesis).
    6.  Hirschmann, A. O. (1945), "National power and structure of foreign
    trade".
    7.  Melnik, A., O. Shy, and R. Stenbacka (2008), "Assessing market dominance"
    <doi:10.1016/j.jebo.2008.03.010>.
    8.  Palma, J. G. (2006). "Globalizing Inequality: 'Centrifugal' and
    'Centripetal' Forces at Work".
    9.  Shannon, C. E. (1948). "A Mathematical Theory of Communication".
    10.  Simpson, E. H. (1949). "Measurement of Diversity"
    <doi:10.1038/163688a0>.
	"""
	
	homepage = "https://github.com/ropensci/concstats/"
	cran = "concstats" 

	version("0.1.6", md5="164a043c64fdcbbadab1180506c1b4ec")

	depends_on("r@2.10:", type=("build", "run"))
