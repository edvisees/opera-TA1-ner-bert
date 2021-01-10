                AIDA Phase 2 Practice Topic Annotations - V2.0
                                 LDC2020E29

                         Linguistic Data Consortium
                               August 28, 2020

0.1 Changes V2.0

This package includes annotations for an additional 16 documents, as
well as quality control corrections to annotations distributed in the
previous version of this package, and updates to the package
documentation.


1. Introduction

This package constitutes the second release of annotations for
documents in the AIDA Phase 2 practice topic annotation set.

The purpose of this annotation is to provide a small sample of the
approach to exhaustive annotation of events, relations, and entities
for Phase 2, and to support a dry run exercise for the TA1
leaderboard-style evaluation.

Annotation of events, relations, and entities is exhaustive for the
selected document regions and selected types, which vary by
document. A file indicating which types and regions are annotated for
each document is included in the docs directory of the release.

Topics covered in this annotation:
T201 - 2014 Disease Outbreak in Venezuela
T202 - 2017 Venezuelan Constituent Assembly Election
T203 - Drone Explosions in Caracas


2. Directory Structure and Content Summary

The directory structure and contents of the package are summarized
below -- paths shown are relative to the base (root) directory of the
package:

  data/                   -- contains subdirectories of annotation by topic
        T201/		  -- subdirectories containing annotation files
                             (see content description below)
        T202/             -- subdirectories containing annotation files
                             (see content description below)
        T203/             -- subdirectories containing annotation files
                             (see content description below)
  docs/                   -- contains documentation about the annotation
                             (see content description below)

2.1 Content Summary

This release contains annotation for a total of 29 unique documents,
with the following distribution across the three practice topics and
languages:

Topic ID    Language   Documents
T201        ENG	       2        
T202        ENG        3
T203        ENG        4
T201        RUS        4
T202        RUS        0
T203        RUS        6
T201        SPA        3
T202        SPA        2
T203        SPA        5

NOTE: The V1.0 README incorrectly stated the package contained
annotations for 15 unique documents, in fact it was 13 documents. The
V2.0 package includes annotation for 16 additional documents, so the
total number of unique documents annotated in the V2.0 package is 29
(not 31).


3. Annotations

The formats of annotations are described in the
AIDA_phase_2_table_field_descriptions_v1.tab file in the docs/
directory; the sections below provide descriptions of the content of
each type of annotation file, with some notes about differences Phase
1 annotation.

3.1 Mentions

There are three mentions tables for each topic: one for entities and
fillers, one for relations, and one for events. These tables contain
information about each annotated mention.

Differences between the mentions.tab files in Phase 2 from those in
Phase 1 include:

- Video mentions no longer specify the signal type (picture or sound),
  so the mediamention_signaltype field in the evt, rel, and arg
  mentions tables is always set to EMPTY_NA

- Video mentions of events and relations include start and end time
  stamps for the mentions (no keyframe id or bounding box
  coordinates); video mentions of entities include bounding
  coordinates and keyframe id (no start and end time stamps)

- Arg mentions include a mention status of "base" or "informative"
  indicating whether the entity/filler mention is the local mention
  that occupies an arg slot in a relation or event mention ("base") or
  whether it is an entity mention that is not connected to an
  event/relation mention but was annotated as part of exhaustive
  annotation of entities by type for the selected regions
  ("informative").

3.2 Slots

There are two slots tables per topic, one for relations and one for
events. Relation and event mentions in the mentions tables must be
looked up in the slots tables to find the arguments and fillers
involved in the relation/event.

Differences between the slots.tab files in Phase 2 from those in Phase
1 include:

- Event mentions can occur as the arguments of other events, in
  addition to occurring as the arguments of relations.

3.3 KB Linking

The KB linking tables in this release provide within-document
coreference of events, relations, and entities. No linking to the
reference knowledge base or cross-document NIL coreference is
included.

NIL ids are provided for each coreference cluster within a
document. Clusters of the "same" entity, relation, or event in
different documents will have different NIL ids since the coreference
annotation is within-document only.


4. Documentation

The following documents are present in the docs/ directory of this
package:

AIDA_Type_Restricted_Event_Relation_Annotation_Guidelines_V1.0.pdf -
current annotation guidelines for exhaustive annotation of event and
relation mentions (including their arguments and attributes)

AIDA_Exhaustive_Entity-Filler_Guidelines_Text_V1.0.pdf - current
guidelines for exhaustive annotation of entities and fillers in text

AIDA_Entity-Filler_Guidelines_Images_V1.1.pdf - current guidelines for
exhaustive annotation of entities and fillers in images and video
keyframes

AIDA_phase_2_table_field_descriptions_v1.tab - description of the
structure of each type of annotation table. This table includes
information about column headers, content of each field, and format of
the contents

doc_lang_topic.tab - provides the root uid, language, and topic for
each document with annotations present in this release

AIDA_Annotation_Ontology_Phase2_V1.1.xlsx - a copy of the annotation
ontology for Phase 2

media_list.tab - provides the child uid and media type for all
non-text assets cited as provenance in the annotations present in this
release.

T201_T202_T203_topic_description_V1.pdf - descriptions of Phase 2
practice topics with queries and query IDs. Note that the queries are
meant to draw annotators attention to expected points of informational
conflict within the topic, but annotation is exhaustive by type for
(the selected regions of) each document; therefore, annotations will
include all event, relation, and entity mentions of the selected
types, regardless of salience to the topics or queries.

doc_regions_types_v5.tab - defines the types and document regions
annotated for each document; one row per type per document
region. Includes root uid, child uid, media type, type, subtype,
subsubtype, and span. Span indicates the range of character offsets
for text and time stamps for video that were annotated for the given
type. For images the span is 'ENTIRE_DOCUMENT_ELEMENT' since the
entire image is in scope for annotation. For entity annotations on
video, the span consists of the keyframe id.


5. Known Issues

The ontology file in the docs directory documents output values for
each type, subtype, subsubtype, and argument role in the tag set. LDC
output uses these output values in all output. There are two known
typos in the tag set:

1. For the relations PersonalSocial.Relationship.n/a and
PersonalSocial.Relationship.Political the output values are
personalsocial.unspecified.unspecified and
personalsocial.unspecified.political, respectively.

2. For the entity/filler type INF.TopicFIller.TopicFIller, note that
the subtype and subsubtype names contain an accidental capitalization
of the "I" in "FIller". The annotation output value, as documented in
the ontology file, and as is true of all output values in LDC's
annotations is entirely lower case.


6. Copyright Information

   (c) 2020 Trustees of the University of Pennsylvania


7. Contact Information

Stephanie Strassel <strassel@ldc.upenn.edu> AIDA PI
Jennifer Tracey <garjen@ldc.upenn.edu> AIDA Project Manager

----
README created by Kira Griffitt on August 18, 2020
       updated by Jennifer Tracey on August 18, 2020
       updated by Kira Griffitt on August 18, 2020
       updated by Kira Griffitt on August 19, 2020
       updated by Kira Griffitt on August 24, 2020
       updated by Kira Griffitt on August 25, 2020
       updated by Kira Griffitt on August 28, 2020
