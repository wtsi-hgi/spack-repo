# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdf5r(RPackage):
	"""Interface to the 'HDF5' Binary Data Format.

	'HDF5' is a data model, library and file format for storing and managing
	large amounts of data. This package provides a nearly feature complete,
	object oriented wrapper for the 'HDF5' API
	<https://support.hdfgroup.org/HDF5/doc/RM/RM_H5Front.html> using R6
	classes. Additionally, functionality is added so that 'HDF5' objects behave
	very similar to their corresponding R counterparts."""

	cran = "hdf5r"

	license("Apache-2.0 OR custom")

	version("1.3.10", md5="6bd2d45695b64a082a88324a901b571c")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-bit64", type=("build", "run"))
	depends_on("hdf5@1.8.13:", type=("build", "link", "run"))

	# The configure script in the package uses the hdf5 h5cc compiler wrapper
	# in the PATH to configure hdf5. That works fine if hdf5 was built with
	# autotools but the hdf5 package in Spack is built with cmake. The compiler
	# wrapper built with cmake does not support the '-show' or '-showconfig'
	# flags. The following patch replaces those commands in the configure
	# script with pkg-config commands.
	patch("configure.patch", when="@:1.3.7")
