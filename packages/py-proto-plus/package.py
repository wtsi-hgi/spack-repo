# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyProtoPlus(PythonPackage):
    """This is a wrapper around protocol buffers. Protocol buffers is a specification format for APIs, such as those inside Google. This library provides protocol buffer message classes and objects that largely behave like native Python types."""

    homepage = "https://github.com/googleapis/proto-plus-python"
    pypi = "proto-plus/proto-plus-1.22.3.tar.gz"

    version("1.22.3", sha256="fdcd09713cbd42480740d2fe29c990f7fbd885a67efc328aa8be6ee3e9f76a6b")

    depends_on("py-protobuf@3.19.0:5.0.0", type=("build", "run"))
