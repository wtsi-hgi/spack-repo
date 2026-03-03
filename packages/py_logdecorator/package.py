# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyLogdecorator(PythonPackage):
    """Move logging code out of your business logic with decorators."""

    homepage = "https://github.com/sighalt/logdecorator"
    pypi = "logdecorator/logdecorator-2.5.tar.gz"

    license("MIT")

    version("2.5", sha256="aa3486b586efa932c56da0b2bfd73d1a93946887220315500bc8e49c55bb864a")
    version("2.4", sha256="7735260e579c50af5f3aee4ee75dab886ae427b1960eb805d8eafe84b75c41b6")
    version("2.2", sha256="8e6d1259cf615b7d2720739a71a3b62dbcfaf22d902382b7d41ac872f4a1d6d9")
    version("2.1", sha256="993bb3f0ccaab169e3a7812d2be411cabb37d38f5d166a1b99b428daaa1dc797")
    version("2.0", sha256="906e3b33b8c48bb7b1e00b83656fda3c9b6c5b928050500a1a9421c445b1b067")
    version("1.0", sha256="f1ab2fabe42cf41a1e9e09f4df85c3aeb52b901ff06d0cbef5bbc79573c0f309")

    depends_on("py-setuptools@61:", type="build")
    depends_on("python@3.6:", type=("build", "run"))
    depends_on("python@3.10:", when="@2.5:", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import logdecorator")
