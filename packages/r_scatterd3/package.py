# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScatterd3(RPackage):
	"""D3 JavaScript Scatterplot from R

	Creates 'D3' 'JavaScript' scatterplots from 'R' with interactive
    features : panning, zooming, tooltips, etc.
	"""
	
	homepage = "https://juba.github.io/scatterD3/"
	cran = "scatterD3" 

	version("1.0.1", md5="f5cff01b015e287cf82e9dd3e6b36458", url="https://cran.r-project.org/src/contrib/scatterD3_1.0.1.tar.gz")

	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
