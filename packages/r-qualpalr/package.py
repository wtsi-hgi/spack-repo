# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQualpalr(RPackage):
	"""Automatic Generation of Qualitative Color Palettes

	Automatic generation of maximally distinct qualitative color palettes,
    optionally tailored to color deficiency. A list of colors or a subspace
    of a color space is used as input and then projected to the DIN99d color space,
    where colors that are maximally distinct are chosen algorithmically.
	"""
	
	homepage = "https://jolars.github.io/qualpalr/"
	cran = "qualpalr" 

	version("0.4.4", md5="d8fc18260c54966da81b783b003217f9")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-randtoolbox@1.17:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-rcpp@0.12.9:", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.7.600.1:", type=("build", "run"))
