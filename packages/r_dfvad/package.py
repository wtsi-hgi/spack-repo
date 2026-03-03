# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDfvad(RPackage):
	"""Diewert and Fox's Method of Value Added Growth Decomposition

	Decomposing value added growth into explanatory factors.
    A cost constrained value added function is defined to specify the 
    production frontier. Industry estimates can also be aggregated using 
    a weighted average approach.
    Details about the methodology and data can be found in Diewert and Fox (2018)
    <doi:10.1093/oxfordhb/9780190226718.013.19>
    and Zeng, Parsons, Diewert and Fox (2018)
    <https://www.business.unsw.edu.au/research-site/centreforappliedeconomicresearch-site/Documents/emg2018-6_SZeng_EMG-Slides.pdf>.
	"""
	
	homepage = "https://github.com/shipei-zeng/dfvad"
	cran = "dfvad" 

	version("0.3.6", md5="d5229d77b473d054973a3f6dde594296")

	depends_on("r@3.5:", type=("build", "run"))
