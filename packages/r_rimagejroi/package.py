# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRimagejroi(RPackage):
	"""Read 'ImageJ' Region of Interest (ROI) Files

	Provides functions to read 'ImageJ' (<http://imagej.nih.gov/ij/>)
    Region of Interest (ROI) files, to plot the ROIs and to convert them to
    'spatstat' (<http://spatstat.org/>) spatial patterns.
	"""
	
	homepage = "https://github.com/davidcsterratt/RImageJROI"
	cran = "RImageJROI" 

	version("0.1.2", md5="286ff6e12035a408b729a5d2b17fde34")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-spatstat@2:", type=("build", "run"))
