# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrenchr(RPackage):
	"""Tools for Microclimate and Biophysical Ecology

	Tools for translating environmental change into organismal response. Microclimate models to vertically scale weather station data to organismal heights. The biophysical modeling tools include both general models for heat flows and specific models to predict body temperatures for a variety of ectothermic taxa. Additional functions model and temporally partition air and soil temperatures and solar radiation. Utility functions estimate the organismal and environmental parameters needed for biophysical ecology. 'TrenchR' focuses on relatively simple and modular functions so users can create transparent and flexible biophysical models. Many functions are derived from Gates (1980) <doi:10.1007/978-1-4612-6024-0> and Campbell and Norman (1988) <isbn:9780387949376>.
	"""
	
	homepage = "https://trenchproject.github.io/TrenchR/"
	cran = "TrenchR" 

	version("1.1.1", md5="c80d339cdd64c959ecbe5778ca562a3e")

	depends_on("r@3.3.1:", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-rdpack@0.7:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
