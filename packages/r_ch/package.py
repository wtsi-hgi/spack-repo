# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCh(RPackage):
	"""About some Small Functions

	The solution to some common problems is proposed, 
     as well as a summary of some small functions. In particular, 
     it provides a useful function for some problems in chemistry.
     For example, monoa(), monob() and mono() function can be used 
     to calculate The pH of weak acid/base. 
     The ggpng() function can save the PNG format with transparent background. 
     The period_table() function will show the periodic table. Also the
     show_ruler() function will show the ruler.
     The show_color() function is funny and easier to show colors.
      I also provide the symb() function to generate multiple symbols at once.
     The csv2vcf() function provides an easy method to generate a file.
     The sym2poly() and sym2coef() function can extract coefficients from 
     polynomials.
	"""
	
	homepage = "https://github.com/tsiamut/ch"
	cran = "ch" 

	version("0.1.0.2", md5="ed2e8ecabbbce0860085c00a95480938")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-clipr", type=("build", "run"))
	depends_on("r-ryacas", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-polynom", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
