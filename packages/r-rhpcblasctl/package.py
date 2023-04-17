# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRhpcblasctl(RPackage):
    """Control the Number of Threads on 'BLAS'

    Control the number of threads on 'BLAS' (Aka 'GotoBLAS', 'OpenBLAS', 'ACML',
    'BLIS' and 'MKL'). And possible to control the number of threads in
    'OpenMP'. Get a number of logical cores and physical cores if feasible."""

    cran = "RhpcBLASctl"

    version("0.23-42", sha256="5c889d5b69e264060b9f1f0383c447f594855b8afc15b7d76d39e4d62b946615")

