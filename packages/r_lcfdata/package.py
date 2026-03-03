# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLcfdata(RPackage):
	"""Data sets for package ``LMERConvenienceFunctions''

	This package contains (1) event-related brain potential data recorded from 10 participants at electrodes Fz, Cz, Pz, and Oz (0--300 ms) in the context of Antoine Tremblay's PhD thesis (Tremblay, 2009); (2) ERP amplitudes at electrode Fz restricted to the 100 to 175 millisecond time window; and (3) plotting data generated from a linear mixed-effects model.
	"""
	
	cran = "LCFdata" 

	version("2.0", md5="584367ae0cb6c90b9f168634286a57db")

	depends_on("r@3:", type=("build", "run"))
