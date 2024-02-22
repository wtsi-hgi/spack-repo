# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class RRjags(RPackage):
	"""Bayesian Graphical Models using MCMC.

	Interface to the JAGS MCMC library."""

	cran = "rjags"

	version("4-15", md5="7c8e06d355256b595dc94cc47385a0f0")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-coda@0.13:", type=("build", "run"))
	depends_on("jags@4:", type=("build", "link", "run"))

	def configure_args(self):
		args = [
			"--with-jags-lib=%s" % self.spec["jags"].prefix.lib,
			"--with-jags-include=%s" % self.spec["jags"].prefix.include,
			"--with-jags-modules=%s/JAGS/modules-4" % self.spec["jags"].prefix.lib,
		]
		return args
