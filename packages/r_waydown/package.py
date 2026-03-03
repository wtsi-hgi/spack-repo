# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWaydown(RPackage):
	"""Computation of Approximate Potentials for Weakly Non-Gradient
Fields

	Computation of approximate potentials for both gradient and non
    gradient fields. It is known from physics that only gradient fields, also
    known as conservative, have a well defined potential function. Here we
    present an algorithm, based on the classical Helmholtz decomposition, to
    obtain an approximate potential function for non gradient fields.
    More information in
    Rodríguez-Sánchez (2020) <doi:10.1371/journal.pcbi.1007788>.
	"""
	
	cran = "waydown" 

	version("1.1.0", md5="999ccb2937b9df21006509f5f64f56db")

	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
