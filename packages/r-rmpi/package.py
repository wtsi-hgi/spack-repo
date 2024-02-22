# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmpi(RPackage):
	"""Interface (Wrapper) to MPI (Message-Passing Interface).

	An interface (wrapper) to MPI APIs. It also provides interactive R manager
	and worker environment."""

	cran = "Rmpi"

	version("0.7-2", md5="ba8538ddb5d4c12863d5b16e3d64f290")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("mpi", type=("build", "link", "run"))

	# The following MPI types are not supported
	conflicts("^intel-mpi")
	conflicts("^intel-parallel-studio")
	conflicts("^mvapich2")
	conflicts("^spectrum-mpi")

	def configure_args(self):
		spec = self.spec

		mpi_name = spec["mpi"].name

		# The type of MPI. Supported values are:
		# OPENMPI, LAM, MPICH, MPICH2, or CRAY
		if mpi_name == "openmpi":
			rmpi_type = "OPENMPI"
		elif mpi_name == "mpich":
			rmpi_type = "MPICH2"
		else:
			raise InstallError("Unsupported MPI type")

		return [
			"--with-Rmpi-type={0}".format(rmpi_type),
			"--with-mpi={0}".format(spec["mpi"].prefix),
		]
