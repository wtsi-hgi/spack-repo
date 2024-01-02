# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCmdstanpy(PythonPackage):
    """CmdStanPy is a lightweight pure-Python interface to CmdStan which provides access to the Stan compiler and all inference algorithms. It supports both development and production workflows. Because model development and testing may require many iterations, the defaults favor development mode and therefore output files are stored on a temporary filesystem. Non-default options allow all aspects of a run to be specified so that scripts can be used to distributed analysis jobs across nodes and machines."""

    homepage = "https://github.com/stan-dev/cmdstanpy"
    pypi = "cmdstanpy/cmdstanpy-1.2.0.tar.gz"

    version("1.2.0", sha256="bdf55ab76f9eea01763b8990a56ff55d03e69ec31d9613fdbbe4c452126ff1bb")

    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-numpy@1.21:", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-stanio", type=("build", "run"))
    depends_on("cmdstan", type="run")
