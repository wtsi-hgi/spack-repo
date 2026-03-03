# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySwiglpk(PythonPackage):
    """swiglpk - Simple swig bindings for the GNU Linear Programming Kit"""

    homepage = "https://github.com/biosustain/swiglpk"
    pypi = "swiglpk/swiglpk-5.0.8.tar.gz"

    version("0.1.0", sha256="fc44aa114aee82870a89665802915796e1a7ee0d0cc3726b0d3d960e14cfd2c1")
    version("1.0.0", sha256="5b25bd8de49442bc5c17244d0fda17f717e8bc494f06d1f7c493d68725b640c2")
    version(
        "1.2.12",
        sha256="38e03647220df8f0ec56732e2f724b6858c508edc4630ed6ffe46806643171f3",
        expand=False,
        url="https://files.pythonhosted.org/packages/50/50/d62ba1a3843ac03a0dee6e1718ccf7c99d094613aff9678f2a5f6d0c2e6f/swiglpk-1.2.12-cp35-cp35m-manylinux1_x86_64.whl",
    )
    version("1.2.13", sha256="f1f41f12e82404c0e67da65c0cbe78433ed6a64a7f22246b753c54fc5db749a1")
    version(
        "1.2.14",
        sha256="2fe565770c6d7475c6419455e6d18a95c718599304f7ee4976b57b297dcff941",
        expand=False,
        url="https://files.pythonhosted.org/packages/71/bb/62f538d969cb2e871e7086e39030279368746b6877724a62a9ffd8870bcb/swiglpk-1.2.14-cp35-cp35m-manylinux1_x86_64.whl",
    )
    version(
        "1.2.15",
        sha256="84afc5616ad3260775cc92eb3faca48901a8f49bd3e013f234c4a0706049c3d8",
        expand=False,
        url="https://files.pythonhosted.org/packages/8f/22/d85165dce55e57498ecd00a38e237688aa2eeede46a25c1ff8c7813a584d/swiglpk-1.2.15-cp35-cp35m-manylinux1_x86_64.whl",
    )
    version(
        "1.2.19",
        sha256="6d49b832673b1246113fbb8b3cb6c05e95937c5f6bcdc188224e4e8de3ec5033",
        expand=False,
        url="https://files.pythonhosted.org/packages/a9/fd/571d1cd18160804bf75e85f7077d7812b73ea54ad36c126a05d66ea84000/swiglpk-1.2.19-cp35-cp35m-manylinux1_x86_64.whl",
    )
    version(
        "1.2.20",
        sha256="86157198fe78da4b8ec517c18b9b7b3f09931ed61f34645b1b2b8b7101c95e48",
        expand=False,
        url="https://files.pythonhosted.org/packages/0e/e4/9f073a33263035d5be4999bcb18e6943bfb33a1c024abf89c45a6a881442/swiglpk-1.2.20-cp35-cp35m-manylinux1_x86_64.whl",
    )
    version(
        "1.2.21",
        sha256="3ffac3ec57f3c2b44f4f12a458dafb4aafe9775aa15304a1370e10a55672cda2",
        expand=False,
        url="https://files.pythonhosted.org/packages/09/b1/fd9529dd97f5d90629b0ff5299f54b817595ce80dc7a048723e6e871c24d/swiglpk-1.2.21-cp35-cp35m-manylinux1_x86_64.whl",
    )
    version(
        "1.2.22",
        sha256="db2b89568e5ab01984108ac15b4f99c487fb54b74e7de1a3f40b1d93c99d6a50",
        expand=False,
        url="https://files.pythonhosted.org/packages/4f/a4/258eed7cffad9e884c6c08b88e5eca15d8f182bd3e5cfb6d7e6353828336/swiglpk-1.2.22-cp35-cp35m-manylinux1_x86_64.whl",
    )
    version(
        "1.3.2rc1",
        sha256="7802048f51b4c43c390be1be2dcfe39670dcf131eab2d9707b244e118ee11cac",
        expand=False,
        url="https://files.pythonhosted.org/packages/df/15/f0f8572b9db7a571d1b04d13096fab159ac093b1577c4c619ad628472dc3/swiglpk-1.3.2rc1-cp35-cp35m-manylinux1_x86_64.whl",
    )
    version(
        "1.3.3",
        sha256="3b062a3b805b638cc18137cf51ee6cc85497f1535fe3a4f17ffe3054c7a9ca4d",
        expand=False,
        url="https://files.pythonhosted.org/packages/22/63/908831b6f6917c6bd489085541c98cc7c27745fa44fae7af85b50e395f8d/swiglpk-1.3.3-cp35-cp35m-manylinux1_x86_64.whl",
    )
    version(
        "1.3.3rc1",
        sha256="34ec6c8aa32645e47f3d8230dcd6003cd46204ba8278adc343a4139a10006db2",
        expand=False,
        url="https://files.pythonhosted.org/packages/f5/ea/5589e52397974ff94cee8c3739a24d85f1ed5444789309748a2d8e7265f1/swiglpk-1.3.3rc1-cp35-cp35m-manylinux1_x86_64.whl",
    )
    version(
        "1.3.3rc2",
        sha256="eeddec91b1dafade07dd11f5f89d5bc6eda81bde9909cecab97a582d1093757d",
        expand=False,
        url="https://files.pythonhosted.org/packages/32/99/6288c7c6874b247d04164f20b8d30d033da2535407d1aa3b67bc6b79afab/swiglpk-1.3.3rc2-cp35-cp35m-manylinux1_x86_64.whl",
    )
    version(
        "1.4.0",
        sha256="69a0c5cea0af0b65706e1a894f23b32874e2898448c1e110e5a5b6792722fd71",
        expand=False,
        url="https://files.pythonhosted.org/packages/10/cf/947595dee8a2bc4763aadfddf83b4ac3c81def63d87fe7ab61f7760de9fb/swiglpk-1.4.0-cp36-cp36m-manylinux1_x86_64.whl",
    )
    version(
        "1.4.0b",
        sha256="3c8bd449f58cb920ac80f77418cbe5583743bea1c52e9f473f3bbdaab5df65f6",
        expand=False,
        url="https://files.pythonhosted.org/packages/34/e2/2a916d5bdf68a83c482e024ac581aac503c646d3b67e5589b0a5e23f12b6/swiglpk-1.4.0b0-cp36-cp36m-manylinux1_x86_64.whl",
    )
    version(
        "1.4.1",
        sha256="dceac93e9af7c169eac4d6d09c256992ba193ad82a9147b3caa053463d9101f3",
        expand=False,
        url="https://files.pythonhosted.org/packages/fb/e8/4fee19ce0444253956cd89033a34c093c79e8a4d8aad7f1552302694aa3b/swiglpk-1.4.1-cp36-cp36m-manylinux1_x86_64.whl",
    )
    version(
        "1.4.1b2",
        sha256="7a4ecf620593b4321317defb229fe92f82ae191e85c9341c61aa141e6b17d7a2",
        expand=False,
        url="https://files.pythonhosted.org/packages/ed/a5/1f9b08817131832c414b8ee4f96d6a18ba5f948285b9c4ea2b012dcf6dd9/swiglpk-1.4.1b2-cp36-cp36m-manylinux1_x86_64.whl",
    )
    version(
        "1.4.3",
        sha256="ba2caed53e8a5074b7106b10028821d7d100dc48adc631fd9cccb876955363db",
        expand=False,
        url="https://files.pythonhosted.org/packages/cb/da/e5b66e1def97e357f0f13496b01fbbea97fc63fa69846e59fba6c563af01/swiglpk-1.4.3-cp36-cp36m-manylinux1_x86_64.whl",
    )
    version(
        "1.4.4",
        sha256="119253b80f61a886dc1a52b5f9d2af766b82cc6ef489d4d076fa68a548a47acd",
        expand=False,
        url="https://files.pythonhosted.org/packages/6f/aa/3bff9bdbb85b8331b32351834a37dad61da13d9deb67570dc1dfe970f646/swiglpk-1.4.4-cp36-cp36m-manylinux1_x86_64.whl",
    )
    version(
        "1.5.0",
        sha256="46260fd78e4a120e26673c96b75de05633ba6d21733c81832fe596e95ae3592f",
        expand=False,
        url="https://files.pythonhosted.org/packages/72/b9/1d9c0fecaff46325c59eb507de149492a7ac421f78517e5a18bc21f08817/swiglpk-1.5.0-cp36-cp36m-manylinux1_x86_64.whl",
    )
    version(
        "1.5.0b",
        sha256="836127f6033e5446c6bae122a99394d08cece2feff3920222271dd352dec8c23",
        expand=False,
        url="https://files.pythonhosted.org/packages/ad/93/7f978f74759ef5cbbdf9354e169839aa3801644336fd2516709155def10f/swiglpk-1.5.0b0-cp36-cp36m-manylinux1_x86_64.whl",
    )
    version(
        "1.5.1",
        sha256="15e837d292ac8f41ba008b89816d34d5d4ddd4b2b3909ee49316e50a3ee8419a",
        expand=False,
        url="https://files.pythonhosted.org/packages/db/6d/e88e5e5e26540346b1817607a88b1665f03c888057b18a685ef1a937768b/swiglpk-1.5.1-cp37-cp37m-manylinux1_x86_64.whl",
    )
    version(
        "4.64.0b",
        sha256="835e60502f23fd7ae6c685f8d60908444c6056a9a5e7a40cf2508ef1776533fc",
        expand=False,
        url="https://files.pythonhosted.org/packages/52/fc/d99e100fd52549a675526f10d934ea0d7b9ac4dd7ca66cb51f9633203799/swiglpk-4.64.0b0-cp37-cp37m-manylinux1_x86_64.whl",
    )
    version(
        "4.65.0",
        sha256="545936cd6bc742bfe8200acd496627cfe41edbfd8df070860a62f4fa88ec3c12",
        expand=False,
        url="https://files.pythonhosted.org/packages/7b/8c/5bb349a9f793b74a6f4b6bc2d6d4d450723d51791a2f1867e316c98db3bc/swiglpk-4.65.0-cp37-cp37m-manylinux1_x86_64.whl",
    )
    version(
        "4.65.1",
        sha256="0f8bc6f30ddbfc5dfcdf22c4efc027d504b542ef84ad29663ecbcbc56d0de35e",
        expand=False,
        url="https://files.pythonhosted.org/packages/41/d6/3cc60e786ba14301b88721af59d230847b60b17d78a5d38373492ef1a11b/swiglpk-4.65.1-cp38-cp38-manylinux1_x86_64.whl",
    )
    version(
        "5.0.0",
        sha256="74adf2a232033656c7b482c3db27b391260d12c114136473c566f87fa7c5494a",
        expand=False,
        url="https://files.pythonhosted.org/packages/bd/85/40f1e6702f406fc91476a4968a26de81720d15cd27ea9177ed5cced6ad63/swiglpk-5.0.0-cp39-cp39-manylinux1_x86_64.whl",
    )
    version("5.0.10", sha256="57ac34ad334da95dd168114bfdb50ae10a2a6a3ddef21e4941f46fe430c5a7e1")
    version("5.0.8", sha256="9b933d7ba17c619f5d838b6b3216647bcf8a2e22cd67ea89b0f2e2f50f7be0ae")

    depends_on("py-setuptools", type=("build"))
    depends_on("glpk")
    depends_on("swig")
    depends_on("gmp")
