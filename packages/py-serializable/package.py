# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySerializable(PythonPackage):
    """Mixin helpers for (de)serialising Python objects."""

    homepage = "https://github.com/openvax/serializable"
    pypi = "serializable/serializable-0.4.1.tar.gz"

    version("0.4.1", sha256="882098d79253d38591a3d4d7d5d78052fce3ba4d29d64c1704d73f1a19d066d8")

    depends_on("py-setuptools", type="build")
    depends_on("py-typechecks@0.0.2:", type=("build", "run"))
    depends_on("py-simplejson", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import serializable")
