# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFloat(RPackage):
	"""32-Bit Floats

	R comes with a suite of utilities for linear algebra with "numeric"
    (double precision) vectors/matrices. However, sometimes single precision (or
    less!) is more than enough for a particular task.  This package extends R's
    linear algebra facilities to include 32-bit float (single precision) data.
    Float vectors/matrices have half the precision of their "numeric"-type
    counterparts but are generally faster to numerically operate on, for a
    performance vs accuracy trade-off.  The internal representation is an S4
    class, which allows us to keep the syntax identical to that of base R's.
    Interaction between floats and base types for binary operators is generally
    possible; in these cases, type promotion always defaults to the higher
    precision.  The package ships with copies of the single precision 'BLAS' and
    'LAPACK', which are automatically built in the event they are not available
    on the system.
	"""
	
	homepage = "https://github.com/wrathematics/float"
	cran = "float" 

	version("0.3-2", md5="5bd17f68abd9d11360b64c21c54816e8")

	depends_on("r@3.6:", type=("build", "run"))
