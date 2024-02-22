# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMrbin(RPackage):
	"""Metabolomics Data Analysis Functions

	A collection of functions for processing and analyzing metabolite data. 
    The namesake function mrbin() converts 1D 
    or 2D Nuclear Magnetic Resonance data into a matrix of values suitable for further data analysis and
    performs basic processing steps in a reproducible way. Negative values, a
    common issue in such data, can be replaced by positive values (<doi:10.1021/acs.jproteome.0c00684>). All used
    parameters are stored in a readable text file and can be restored from that
    file to enable exact reproduction of the data at a later time. The function fia() ranks features according
    to their impact on classifier models, especially artificial neural network models.
	"""
	
	homepage = "http://www.kleinomicslab.com/software/"
	cran = "mrbin" 

	version("1.7.4", md5="d08dd163444d41e5a543d00c47fb64f0")

	depends_on("r@2.10:", type=("build", "run"))
