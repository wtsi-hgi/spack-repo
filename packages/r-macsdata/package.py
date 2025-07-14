# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMacsdata(RPackage):
	"""Test datasets for the MACSr package

	Test datasets from the MACS3 test examples are use in the examples of the `MACSr` package. All 9 datasets are uploaded to the `ExperimentHub`. The original data can be found at: https://github.com/macs3-project/MACS/.
	"""
	
	bioc = "MACSdata"

	version("1.16.0", commit="894683e454856ee89f187613a20aa678ed0bc81c")
	version("1.10.0", commit="43b7147cb5d716e487843e7b4d6d41ad8497e712")


