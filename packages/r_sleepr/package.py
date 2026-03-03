# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSleepr(RPackage):
	"""Analyse Activity and Sleep Behaviour

	Use behavioural variables to score activity and infer sleep from bouts of immobility. 
    It is primarily designed to score sleep in fruit flies from Drosophila Activity Monitor (TriKinetics) and Ethoscope data.
    It implements sleep scoring using the "five-minute rule" (Hendricks et al. (2000) <DOI:10.1016/S0896-6273(00)80877-6>),
    activity classification for Ethoscopes (Geissmann et al. (2017) <DOI:10.1371/journal.pbio.2003026>) 
    and a new algorithm to detect when animals are dead.
	"""
	
	homepage = "https://github.com/rethomics/sleepr"
	cran = "sleepr" 

	version("0.3.0", md5="aa3f96051d16260d370b8de4e5108bd1")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-behavr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
