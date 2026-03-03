# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSdclog(RPackage):
	"""Tools for Statistical Disclosure Control in Research Data
Centers

	Tools for researchers to explicitly show that their results
    comply to rules for statistical disclosure control imposed by research
    data centers. These tools help in checking descriptive statistics and
    models and in calculating extreme values that are not individual data.
    Also included is a simple function to create log files. The methods
    used here are described in the "Guidelines for the checking of output
    based on microdata research" by Bond, Brandt, and de Wolf (2015)
    <https://ec.europa.eu/eurostat/cros/system/files/dwb_standalone-document_output-checking-guidelines.pdf>.
	"""
	
	homepage = "https://github.com/matthiasgomolka/sdcLog"
	cran = "sdcLog" 

	version("0.5.0", md5="8da29db7797e2ebc736f29982848b912")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-broom@0.5.5:", type=("build", "run"))
	depends_on("r-checkmate@2:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-data-table@1.12.8:", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
