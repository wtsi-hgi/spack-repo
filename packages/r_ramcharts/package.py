# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRamcharts(RPackage):
	"""JavaScript Charts Tool

	Provides an R interface for using 'AmCharts' Library. Based on
    'htmlwidgets', it provides a global architecture to generate 'JavaScript' source
    code for charts. Most of classes in the library have their equivalent in R
    with S4 classes; for those classes, not all properties have been referenced but
    can easily be added in the constructors. Complex properties (e.g. 'JavaScript'
    object) can be passed as named list. See examples at 
    <https://datastorm-open.github.io/introduction_ramcharts/> 
    and <https://www.amcharts.com/> for
    more information about the library. The package includes the free version
    of 'AmCharts' Library. Its only limitation is a small link to the web site
    displayed on your charts. If you enjoy this library, do not hesitate to refer
    to this page <https://www.amcharts.com/online-store/> to purchase a licence,
    and thus support its creators and get a period of Priority Support. See also
    <https://www.amcharts.com/about/> for more information about 'AmCharts' company.
	"""
	
	homepage = "https://datastorm-open.github.io/introduction_ramcharts/"
	cran = "rAmCharts" 

	version("2.1.15", md5="882dfbce2ce0a1accec8b3228f85e75a")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-data-table@1.9.6:", type=("build", "run"))
	depends_on("r-piper", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
