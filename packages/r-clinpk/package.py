# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClinpk(RPackage):
	"""Clinical Pharmacokinetics Toolkit

	Provides equations commonly used in clinical
        pharmacokinetics and clinical pharmacology, such as equations
        for dose individualization, compartmental pharmacokinetics,
        drug exposure, anthropomorphic calculations, clinical
        chemistry, and conversion of common clinical parameters. Where
        possible and relevant, it provides multiple published and
        peer-reviewed equations within the respective R function.
	"""
	
	homepage = "https://github.com/InsightRX/clinPK"
	cran = "clinPK" 

	version("0.13.0", md5="f4b5b44161c5257fb5cf218cbea1706c")
	version("0.11.1", md5="7fcc89631f75a382d91acb300febfc53")

