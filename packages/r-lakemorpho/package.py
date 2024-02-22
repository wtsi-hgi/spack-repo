# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLakemorpho(RPackage):
	"""Lake Morphometry Metrics

	Lake morphometry metrics are used by limnologists to understand,
    among other things, the ecological processes in a lake. Traditionally, these
    metrics are calculated by hand, with planimeters, and increasingly with
    commercial GIS products. All of these methods work; however, they are either
    outdated, difficult to reproduce, or require expensive licenses to use. The
    'lakemorpho' package provides the tools to calculate a typical suite
    of these metrics from an input elevation model and lake polygon. The metrics
    currently supported are: fetch, major axis, minor axis, major/minor axis 
    ratio, maximum length, maximum width, mean width, maximum depth, mean depth, 
    shoreline development, shoreline length, surface area, and volume.
	"""
	
	homepage = "https://github.com/jhollist/lakemorpho/"
	cran = "lakemorpho" 

	version("1.3.2", md5="e2f8a20e32b6a1ce5234dab9c8508cbd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
