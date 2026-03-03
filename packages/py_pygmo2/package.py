# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPygmo2(CMakePackage):
    """pygmo is a scientific Python library for massively parallel optimization. It is built around the idea of providing a unified interface to optimization algorithms and to optimization problems and to make their deployment in massively parallel environments easy."""

    url = "https://github.com/esa/pygmo2/archive/refs/tags/v2.19.5.tar.gz"

    version("2.19.5", sha256="742ff0c3d535cb2af94d5095968d8f29c23ed7bdbd4ddd8259ca787eef881aa2")
    version("2.19.4", sha256="ee74d51cdeabc9bfe54280cd26b15a2722126e6e97edae2d41c9fda871a81988")
    version("2.19.3", sha256="40c3bcaaa0938a1acea1c31400f0d015faa38ae82fee8686cae392728e73e96f")
    version("2.19.2", sha256="6480b2c7c4fc4a53966e331737d4e17bd987972856550d4896c10cc8c08ea39f")
    version("2.19.1", sha256="b758a0bc4143a76cd5019ac5111b11ff7967722b3cedf6f48f69df63e56f9aa2")
    version("2.19.0", sha256="96b3e412fd264ca74204b6d66aec51c67a7a6909501deae0e4bc263b88e4f176")
    version("2.18.0", sha256="9f081cc973297894af09f713f889870ac452bfb32b471f9f7ba08a5e0bb9a125")
    version("2.16.1", sha256="54d4fa99e4bff539fca67dfcdc909499fd3f1a3186f7c7fc8200f19512954166")
    version("2.16.0", sha256="9b202fa329186f9ba8297f640f885f009876ee0884789fa972636c401b5ce8b8")
    version("2.15.0", sha256="0f45636d47d5309f5f3d771e6677437f9d8de96cbad8b4f2758fa79c856022cc")

    depends_on("pagmo", type=("build", "link", "run"))
