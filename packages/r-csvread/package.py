# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCsvread(RPackage):
	"""Fast Specialized CSV File Loader

	Functions for loading large (10M+ lines) CSV
    and other delimited files, similar to read.csv, but typically faster and
    using less memory than the standard R loader. While not entirely general,
    it covers many common use cases when the types of columns in the CSV file
    are known in advance. In addition, the package provides a class 'int64',
    which represents 64-bit integers exactly when reading from a file. The
    latter is useful when working with 64-bit integer identifiers exported from
    databases. The CSV file loader supports common column types including
    'integer', 'double', 'string', and 'int64', leaving further type
    transformations  to the user.
	"""
	
	homepage = "https://github.com/jabiru/csvread"
	cran = "csvread" 

	version("1.2.2", md5="84c1bea4924a8f09b3dc8bfa3c76a784")

	depends_on("r@2.15:", type=("build", "run"))
