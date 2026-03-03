# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyLibplinkio(PythonPackage):
    """Python bindings for libplinkio: a library for parsing PLINK genotype files."""

    homepage = "https://github.com/mfranberg/libplinkio"
    url = "https://github.com/mfranberg/libplinkio/archive/refs/tags/v0.9.8.tar.gz"
    git = "https://github.com/mfranberg/libplinkio.git"

    license("BSD-3-Clause")

    version("0.9.8", sha256="de54dd4789b2da9b937a1f445dc6976153211dc35b4376a4cf561ad2ee861075")

    # Build dependencies
    depends_on("py-setuptools", type="build")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            # No CLI; perform a basic import test
            python("-c", "import plinkio")

