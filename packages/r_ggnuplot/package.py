# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgnuplot(RPackage):
	"""Make 'ggplot2' Look Like 'gnuplot'

	Provides a theme, a discrete color palette, and continuous scales
    to make 'ggplot2' look like 'gnuplot'. This may be helpful if you use both
    'ggplot2' and 'gnuplot' in one project.
	"""
	
	homepage = "https://github.com/hriebl/ggnuplot"
	cran = "ggnuplot" 

	version("0.1.0", md5="381db9627f050e48bb69b6469957124b")

	depends_on("r-ggplot2", type=("build", "run"))
