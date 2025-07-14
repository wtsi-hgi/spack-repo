# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTopdownrdata(RPackage):
	"""Example Files for the topdownr R Package

	Example data for the topdownr package generated on a Thermo Orbitrap Fusion Lumos MS device.
	"""
	
	homepage = "https://github.com/sgibb/topdownrdata/"
	bioc = "topdownrdata"

	version("1.30.0", commit="b78a03a9bc295eeafb47c6cb45a117a11439188a")
	version("1.24.0", commit="b6233105fb260cca95d72641043b84ee9b51a4e2")

	depends_on("r-topdownr", type=("build", "run"))

