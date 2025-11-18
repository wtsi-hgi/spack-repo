# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgtranscript(RPackage):
	"""ggtranscript is a ggplot2 extension that makes it to easy to visualize transcript structure and annotation."""
	
	homepage = "https://github.com/dzhang32/ggtranscript/"
	git = "https://github.com/dzhang32/ggtranscript.git" 

	version("1.0.0", commit="682a0df688ad242fa262d0b0557bf973dc202787")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
