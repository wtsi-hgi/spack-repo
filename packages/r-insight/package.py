# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInsight(RPackage):
    """Easy Access to Model Information for Various Model Objects.

    A tool to provide an easy, intuitive and consistent access to information
    contained in various R models, like model formulas, model terms,
    information about random effects, data that was used to fit the model or
    data from response variables. 'insight' mainly revolves around two types of
    functions: Functions that find (the names of) information, starting with
    'find_', and functions that get the underlying data, starting with 'get_'.
    The package has a consistent syntax and works with many different model
    objects, where otherwise functions to access these information are
    missing."""

    cran = "insight"

    version("0.19.5", sha256="6f429fc8c760ff0a47d353d7da212a4ce32f51c5daa8c9dc694152b65aba241d")
    version("0.19.4", sha256="e1a5c49e0ac873094edc779c1cfbe195fd672e7125257fe70b09e74c582925ed")
    version("0.19.3", sha256="ff1f39b15e84f671f1602e5f7ef646d0f1c25ea63ad87c272a58e25d8b8d887e")
    version("0.19.2", sha256="77abc57789b0b79ff00f36db3f0037aaa962278148c01f8579c2e9d695c62976")
    version("0.19.1", sha256="1042629644c66b1a372fd4471d38adccc0c3a329879ef685b14b65575c1c98eb")
    version("0.19.0", sha256="e7b63d394eb86c12cfba56178f12bc3bed86d19421bdb5e691c884add9922025")
    version("0.18.8", sha256="f52adaea67d36a333e8c430b85af50a581dbd5543390cd1f282502e4103f7505")
    version("0.18.7", sha256="720c116978fac5409c3e4320486ddfcc33c11269534550f17e5ce6fabb5575e6")
    version("0.18.6", sha256="ab0dc3c8ec765f2e93f7bcc3a7abb05140f71db24d50bf8cdd595a5a4e771cae")
    version("0.18.5", sha256="653a51b1c32de06e4649ffdd209e51c9cd82986ad6f8d5a3bcdedb6911456652")
    version("0.18.4", sha256="6e3f378bc2eb30c0300103bdd8a3e74371199b36867b45978ec9690a6fda0c5f")
    version("0.18.3", sha256="0922867dc00b19d22d1db4e92233b2e7884f78f0fe1f421656b90d1b236d46ae")
    version("0.18.2", sha256="979b6a12d846315ba3b594744b28062fbb037807b8bc935933d6c195c3ccef54")
    version("0.18.0", sha256="41adc29f73aa37b95cfa7c84df3c025352926a2bd0989909e2180a84989af725")
    version("0.17.1", sha256="653c5542a0c953ad4b75800e2ab52eed244e1e698aa5bc9fc64dc657a3cece35")
    version("0.17.0", sha256="37994d9014de93f729f67757b9c262dcefb8e2153df8513f03c58fe72df2ace7")
    version("0.16.0", sha256="7944d7a386c99ea06d9d9e2b5f4aeb98fded7ec90b1cb908d03e278480be9e3d")
    version("0.15.0", sha256="d6a148c3e1cfcb3829e2f8950bcbf98f500ee88bebd7e2482f9b085542e93fee")
    version("0.14.5", sha256="ddf1afe506732e83468d5e7425b00d60e9ce836a544da2d68d513b289e386c82")
    version("0.14.4", sha256="434f3c97df06ab5b885d0b82c30b8d8a7fdaca3bcbff98e4fa6cfd3346b6c340")
    version("0.14.3", sha256="98242bff799977464fc97814857ee38e6a03041b127fbe7c28b0f210768bd6bb")
    version("0.14.2", sha256="f7a117cc65bab251fb39a67bf7891d334947179966e628fbd43eb2b49ca9c737")
    version("0.14.1", sha256="0e7761997a46ee33039cdeff1779dbc210de3644e4444c6e893e4ef2f12cc129")
    version("0.14.0", sha256="96b637e905a8abcbd46d300e9c3d6681a68d038a1b936fc46e3b3d2ce47471fe")
    version("0.13.2", sha256="4126900e779e7bee819628d750e4c55eab2bc7652b02127588b50878429b670d")
    version("0.13.1", sha256="b478805346ef3f9974fc8e9af0d1a1bfddfd0c8df12b5b959dd625ea7ef744d1")
    version("0.13.0", sha256="f65013249f888118cec6fcdaf19ad828d73001addb01371a01240c577135d9a2")
    version("0.12.0", sha256="faf89f83aa217c5c82e0bc65c820684e75f2547ebfdfec5ea03889d312677b3e")
    version("0.11.1", sha256="600a7b8e15ef00b38fc5d7652a36794d7465e66a5bbed73afe6b86a8b6eb25d5")
    version("0.11.0", sha256="ef643e93e6f6bde9a1de58967e5b7b1f60671765720775c9ea63ae895f3b4831")
    version("0.10.0", sha256="519a85a0e96126a2cc212b6a0fe202da98f116e3065747a3fa83b00d07559be4")
    version("0.9.6", sha256="10342e5256e23ec223f6833c5340fc624aa34005faac67ac1d78396cc2d0bc96")
    version("0.9.5", sha256="b1ba4540264e1d35fbf65f2a0a6f5b44cbce2776bd16f8c4472c4e24099ea320")
    version("0.9.1", sha256="46f16c89321c0b70e7c371439bff954050b26f3e8739deff3ae057a0cbfbde34")
    version("0.9.0", sha256="74e3c0c2b8634c7e801c19b0a01004b6cc09a3b898561a0229aa8e580b434caa")
    version("0.8.5", sha256="f3f8c33902eb9359d5770a32fab884eeabcfff941bf7eeeda46c8a109afcec3d")
    version("0.8.4", sha256="619393b2cd5019dad5834611e16086120522a4cf31466502b9d7d6cf00ea4936")
    version("0.8.3", sha256="d2a3f53a9d548909d50a74b67a369169d122beed62ca5ef90db822333251a552")
    version("0.8.2", sha256="92d13b26e0a72ab1d846a0ca3653c07a868fc878f7f6f897c347857d793b4e3a")
    version("0.8.1", sha256="e6c4ee2754651530f5d67a14ca172fa4d5190dedc6b52530bb23cadafc4a08f9")
    version("0.8.0", sha256="60b24aab1e068e489db90e9a6fa603db7c1cbd201d7574c824987877e5e66cae")
    version("0.7.1", sha256="4d3505ee53e103979f4a2d32e4151787bab2c3ed5460c7d3e25af18d51ae9269")
    version("0.7.0", sha256="588be1495c1604f9fe3f64e322e49096b45ec541a20e946ef3a18d3c10619daa")
    version("0.6.0", sha256="cd1dedc4c8e97c55831f4cf802c32112d06c22d0ef18f55811d3ff072481f8c7")
    version("0.5.0", sha256="d7d9929f29cf0453cfa79dde35ba57d96a45adf95ddbf9ffb0a97d6113153053")
    version("0.4.1", sha256="02fd38e8a9a407501570daff89b6b9dc2e0d34a4dfc9227ebae59fb4eac881d3")
    version("0.4.0", sha256="2f1f4ba65fa3cf424364a76e5071d3a74bb58015f5dc1fce73a1433f14ce7e78")
    version("0.3.0", sha256="6b9fcaeb81561593f73133640c04dfe20f74b80343ab68c7ccfeb200184448e4")
    version("0.2.0", sha256="3fea8a97a1641e58fcaaa1285a3a3094965fa631b316d0c69697e28e4b63c93a")
    version("0.1.2", sha256="aee8f96482c4b458f5b64794379a9c765564f9e768d7263304c9e4548904c033")

    depends_on("r@3.4:", type=("build", "run"))
    depends_on("r@3.5:", type=("build", "run"), when="@0.18.4:")
