# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReactablefmtr(RPackage):
	"""Streamlined Table Styling and Formatting for Reactable

	Provides various features to streamline and enhance the styling of interactive 
    reactable tables with easy-to-use and highly-customizable functions and themes. 
    Apply conditional formatting to cells with data bars, color scales, color tiles,
    and icon sets. Utilize custom table themes inspired by popular websites such 
    and bootstrap themes. Apply sparkline line & bar charts 
    (note this feature requires the 'dataui' package which can be downloaded from
    <https://github.com/timelyportfolio/dataui>).
    Increase the portability and reproducibility of reactable tables by embedding images 
    from the web directly into cells. Save the final table output as a static image or 
    interactive file.
	"""
	
	homepage = "https://kcuilla.github.io/reactablefmtr/"
	cran = "reactablefmtr" 

	version("2.0.0", md5="cb17787794aea60c46ba04fa155308b9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-reactable@0.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-htmlwidgets@1.5.3:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-sass@0.4:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tippy@0.1:", type=("build", "run"))
	depends_on("r-webshot", type=("build", "run"))
