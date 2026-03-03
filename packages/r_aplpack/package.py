# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAplpack(RPackage):
	"""Another Plot Package: 'Bagplots', 'Iconplots', 'Summaryplots',
Slider Functions and Others

	Some functions for drawing some special plots:
   The function 'bagplot' plots a bagplot,
   'faces' plots chernoff faces,
   'iconplot' plots a representation of a frequency table or a data matrix,
   'plothulls' plots hulls of a bivariate data set,
   'plotsummary' plots a graphical summary of a data set,
   'puticon' adds icons to a plot,
   'skyline.hist' combines several histograms of a one dimensional data set in one plot,
   'slider' functions supports some interactive graphics,
   'spin3R' helps an inspection of a 3-dim point cloud,
   'stem.leaf' plots a stem and leaf plot,
   'stem.leaf.backback' plots back-to-back versions of stem and leaf plot.
	"""
	
	homepage = "https://www.uni-bielefeld.de/fakultaeten/wirtschaftswissenschaften/fakultaet/lehrende-ehemalige/pwolf/wolf_aplpack/index.xml"
	cran = "aplpack" 

	version("1.3.5", md5="b21426d7246139da14f3d6280b53ac72")

	depends_on("r@3:", type=("build", "run"))
