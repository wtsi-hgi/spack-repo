# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSfinx(RPackage):
	"""Straightforward Filtering Index for AP-MS Data Analysis (SFINX)

	The straightforward filtering index (SFINX) identifies true positive
    protein interactions in a fast, user-friendly, and highly accurate way.
    It is not only useful for the filtering of affinity purification -
    mass spectrometry (AP-MS) data, but also for similar types of data
    resulting from other co-complex interactomics technologies, such as TAP-MS,
    Virotrap and BioID. SFINX can also be used via the website interface at
    <http://sfinx.ugent.be>.
	"""
	
	homepage = "http://sfinx.ugent.be"
	cran = "sfinx" 

	version("1.7.99", md5="d8c5646f4294d2f97730c2188071add9")

	depends_on("r@3.2.3:", type=("build", "run"))
