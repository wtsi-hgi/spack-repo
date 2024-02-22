# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGggibbous(RPackage):
	"""Moon Charts, a Pie Chart Alternative

	Moon charts are like pie charts except that the proportions are
    shown as crescent or gibbous portions of a circle, like the lit and unlit
    portions of the moon. As such, they work best with only one or two groups.
    'gggibbous' extends 'ggplot2' to allow for plotting multiple moon charts in
    a single panel and does not require a square coordinate system.
	"""
	
	homepage = "https://github.com/mnbram/gggibbous"
	cran = "gggibbous" 

	version("0.1.1", md5="75c188ad55e78850eb954ddd0bd146f9")

	depends_on("r-ggplot2@3.2.1:", type=("build", "run"))
	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-scales@1:", type=("build", "run"))
